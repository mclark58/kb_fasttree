# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport
import time


class DataFileUtil(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login',
            service_ver='release',
            async_job_check_time_ms=100, async_job_check_time_scale_percent=150, 
            async_job_check_max_time_ms=300000):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = service_ver
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc,
            async_job_check_time_ms=async_job_check_time_ms,
            async_job_check_time_scale_percent=async_job_check_time_scale_percent,
            async_job_check_max_time_ms=async_job_check_max_time_ms)

    def _check_job(self, job_id):
        return self._client._check_job('DataFileUtil', job_id)

    def _shock_to_file_submit(self, params, context=None):
        return self._client._submit_job(
             'DataFileUtil.shock_to_file', [params],
             self._service_ver, context)

    def shock_to_file(self, params, context=None):
        """
        Download a file from Shock.
        :param params: instance of type "ShockToFileParams" (Input for the
           shock_to_file function. Required parameters: shock_id | handle_id
           - the ID of the Shock node, or the Handle to a shock node.
           file_path - the location to save the file output. If this is a
           directory, the file will be named as per the filename in Shock.
           Optional parameters: unpack - either null, 'uncompress', or
           'unpack'. 'uncompress' will cause any bzip or gzip files to be
           uncompressed. 'unpack' will behave the same way, but it will also
           unpack tar and zip archive files (uncompressing gzipped or bzipped
           archive files if necessary). If 'uncompress' is specified and an
           archive file is encountered, an error will be thrown. If the file
           is an archive, it will be unbundled into the directory containing
           the original output file. Note that if the file name (either as
           provided by the user or by Shock) without the a decompression
           extension (e.g. .gz, .zip or .tgz -> .tar) points to an existing
           file and unpack is specified, that file will be overwritten by the
           decompressed Shock file.) -> structure: parameter "shock_id" of
           String, parameter "handle_id" of String, parameter "file_path" of
           String, parameter "unpack" of String
        :returns: instance of type "ShockToFileOutput" (Output from the
           shock_to_file function. node_file_name - the filename of the file
           as stored in Shock. file_path - the path to the downloaded file.
           If a directory was specified in the input, this will be the
           directory appended with the shock file name. If a file was
           specified, it will be that file path. In either case, if the file
           is uncompressed any compression file extensions will be removed
           (e.g. .gz) and or altered (e.g. .tgz -> .tar) as appropriate. size
           - the size of the file in bytes as stored in Shock, prior to
           unpacking. attributes - the file attributes, if any, stored in
           Shock.) -> structure: parameter "node_file_name" of String,
           parameter "file_path" of String, parameter "size" of Long,
           parameter "attributes" of mapping from String to unspecified object
        """
        job_id = self._shock_to_file_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _shock_to_file_mass_submit(self, params, context=None):
        return self._client._submit_job(
             'DataFileUtil.shock_to_file_mass', [params],
             self._service_ver, context)

    def shock_to_file_mass(self, params, context=None):
        """
        Download multiple files from Shock.
        :param params: instance of list of type "ShockToFileParams" (Input
           for the shock_to_file function. Required parameters: shock_id |
           handle_id - the ID of the Shock node, or the Handle to a shock
           node. file_path - the location to save the file output. If this is
           a directory, the file will be named as per the filename in Shock.
           Optional parameters: unpack - either null, 'uncompress', or
           'unpack'. 'uncompress' will cause any bzip or gzip files to be
           uncompressed. 'unpack' will behave the same way, but it will also
           unpack tar and zip archive files (uncompressing gzipped or bzipped
           archive files if necessary). If 'uncompress' is specified and an
           archive file is encountered, an error will be thrown. If the file
           is an archive, it will be unbundled into the directory containing
           the original output file. Note that if the file name (either as
           provided by the user or by Shock) without the a decompression
           extension (e.g. .gz, .zip or .tgz -> .tar) points to an existing
           file and unpack is specified, that file will be overwritten by the
           decompressed Shock file.) -> structure: parameter "shock_id" of
           String, parameter "handle_id" of String, parameter "file_path" of
           String, parameter "unpack" of String
        :returns: instance of list of type "ShockToFileOutput" (Output from
           the shock_to_file function. node_file_name - the filename of the
           file as stored in Shock. file_path - the path to the downloaded
           file. If a directory was specified in the input, this will be the
           directory appended with the shock file name. If a file was
           specified, it will be that file path. In either case, if the file
           is uncompressed any compression file extensions will be removed
           (e.g. .gz) and or altered (e.g. .tgz -> .tar) as appropriate. size
           - the size of the file in bytes as stored in Shock, prior to
           unpacking. attributes - the file attributes, if any, stored in
           Shock.) -> structure: parameter "node_file_name" of String,
           parameter "file_path" of String, parameter "size" of Long,
           parameter "attributes" of mapping from String to unspecified object
        """
        job_id = self._shock_to_file_mass_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _file_to_shock_submit(self, params, context=None):
        return self._client._submit_job(
             'DataFileUtil.file_to_shock', [params],
             self._service_ver, context)

    def file_to_shock(self, params, context=None):
        """
        Load a file to Shock.
        :param params: instance of type "FileToShockParams" (Input for the
           file_to_shock function. Required parameters: file_path - the
           location of the file (or directory if using the pack parameter) to
           load to Shock. Optional parameters: attributes - user-specified
           attributes to save to the Shock node along with the file.
           make_handle - make a Handle Service handle for the shock node.
           Default false. pack - compress a file or archive a directory
           before loading to Shock. The file_path argument will be appended
           with the appropriate file extension prior to writing. For gzips
           only, if the file extension denotes that the file is already
           compressed, it will be skipped. If file_path is a directory and
           tarring or zipping is specified, the created file name will be set
           to the directory name, possibly overwriting an existing file.
           Attempting to pack the root directory is an error. Do not attempt
           to pack the scratch space root as noted in the module description.
           The allowed values are: gzip - gzip the file given by file_path.
           targz - tar and gzip the directory specified by the directory
           portion of the file_path into the file specified by the file_path.
           zip - as targz but zip the directory.) -> structure: parameter
           "file_path" of String, parameter "attributes" of mapping from
           String to unspecified object, parameter "make_handle" of type
           "boolean" (A boolean - 0 for false, 1 for true. @range (0, 1)),
           parameter "pack" of String
        :returns: instance of type "FileToShockOutput" (Output of the
           file_to_shock function. shock_id - the ID of the new Shock node.
           handle - the new handle, if created. Null otherwise.
           node_file_name - the name of the file stored in Shock. size - the
           size of the file stored in shock.) -> structure: parameter
           "shock_id" of String, parameter "handle" of type "Handle" (A
           handle for a file stored in Shock. hid - the id of the handle in
           the Handle Service that references this shock node id - the id for
           the shock node url - the url of the shock server type - the type
           of the handle. This should always be shock. file_name - the name
           of the file remote_md5 - the md5 digest of the file.) ->
           structure: parameter "hid" of String, parameter "file_name" of
           String, parameter "id" of String, parameter "url" of String,
           parameter "type" of String, parameter "remote_md5" of String,
           parameter "node_file_name" of String, parameter "size" of String
        """
        job_id = self._file_to_shock_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _unpack_file_submit(self, params, context=None):
        return self._client._submit_job(
             'DataFileUtil.unpack_file', [params],
             self._service_ver, context)

    def unpack_file(self, params, context=None):
        """
        Using the same logic as unpacking a Shock file, this method will cause
        any bzip or gzip files to be uncompressed, and then unpack tar and zip
        archive files (uncompressing gzipped or bzipped archive files if 
        necessary). If the file is an archive, it will be unbundled into the 
        directory containing the original output file.
        :param params: instance of type "UnpackFileParams" -> structure:
           parameter "file_path" of String
        :returns: instance of type "UnpackFileResult" -> structure: parameter
           "file_path" of String
        """
        job_id = self._unpack_file_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _pack_file_submit(self, params, context=None):
        return self._client._submit_job(
             'DataFileUtil.pack_file', [params],
             self._service_ver, context)

    def pack_file(self, params, context=None):
        """
        Pack a file or directory into gzip, targz, or zip archives.
        :param params: instance of type "PackFileParams" (Input for the
           pack_file function. Required parameters: file_path - the location
           of the file (or directory if using the pack parameter) to load to
           Shock. pack - The format into which the file or files will be
           packed. The file_path argument will be appended with the
           appropriate file extension prior to writing. For gzips only, if
           the file extension denotes that the file is already compressed, it
           will be skipped. If file_path is a directory and tarring or
           zipping is specified, the created file name will be set to the
           directory name, possibly overwriting an existing file. Attempting
           to pack the root directory is an error. Do not attempt to pack the
           scratch space root as noted in the module description. The allowed
           values are: gzip - gzip the file given by file_path. targz - tar
           and gzip the directory specified by the directory portion of the
           file_path into the file specified by the file_path. zip - as targz
           but zip the directory.) -> structure: parameter "file_path" of
           String, parameter "pack" of String
        :returns: instance of type "PackFileResult" (Output from the
           pack_file function. file_path - the path to the packed file.) ->
           structure: parameter "file_path" of String
        """
        job_id = self._pack_file_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _package_for_download_submit(self, params, context=None):
        return self._client._submit_job(
             'DataFileUtil.package_for_download', [params],
             self._service_ver, context)

    def package_for_download(self, params, context=None):
        """
        :param params: instance of type "PackageForDownloadParams" (Input for
           the package_for_download function. Required parameters: file_path
           - the location of the directory to compress as zip archive before
           loading to Shock. This argument will be appended with the '.zip'
           file extension prior to writing. If it is a directory, file name
           of the created archive will be set to the directory name followed
           by '.zip', possibly overwriting an existing file. Attempting to
           pack the root directory is an error. Do not attempt to pack the
           scratch space root as noted in the module description. ws_ref -
           list of references to workspace objects which will be used to
           produce info-files in JSON format containing workspace metadata
           and provenance structures. It produces new files in folder pointed
           by file_path (or folder containing file pointed by file_path if
           it's not folder). Optional parameters: attributes - user-specified
           attributes to save to the Shock node along with the file.) ->
           structure: parameter "file_path" of String, parameter "attributes"
           of mapping from String to unspecified object, parameter "ws_refs"
           of list of String
        :returns: instance of type "PackageForDownloadOutput" (Output of the
           package_for_download function. shock_id - the ID of the new Shock
           node. node_file_name - the name of the file stored in Shock. size
           - the size of the file stored in shock.) -> structure: parameter
           "shock_id" of String, parameter "node_file_name" of String,
           parameter "size" of String
        """
        job_id = self._package_for_download_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _file_to_shock_mass_submit(self, params, context=None):
        return self._client._submit_job(
             'DataFileUtil.file_to_shock_mass', [params],
             self._service_ver, context)

    def file_to_shock_mass(self, params, context=None):
        """
        Load multiple files to Shock.
        :param params: instance of list of type "FileToShockParams" (Input
           for the file_to_shock function. Required parameters: file_path -
           the location of the file (or directory if using the pack
           parameter) to load to Shock. Optional parameters: attributes -
           user-specified attributes to save to the Shock node along with the
           file. make_handle - make a Handle Service handle for the shock
           node. Default false. pack - compress a file or archive a directory
           before loading to Shock. The file_path argument will be appended
           with the appropriate file extension prior to writing. For gzips
           only, if the file extension denotes that the file is already
           compressed, it will be skipped. If file_path is a directory and
           tarring or zipping is specified, the created file name will be set
           to the directory name, possibly overwriting an existing file.
           Attempting to pack the root directory is an error. Do not attempt
           to pack the scratch space root as noted in the module description.
           The allowed values are: gzip - gzip the file given by file_path.
           targz - tar and gzip the directory specified by the directory
           portion of the file_path into the file specified by the file_path.
           zip - as targz but zip the directory.) -> structure: parameter
           "file_path" of String, parameter "attributes" of mapping from
           String to unspecified object, parameter "make_handle" of type
           "boolean" (A boolean - 0 for false, 1 for true. @range (0, 1)),
           parameter "pack" of String
        :returns: instance of list of type "FileToShockOutput" (Output of the
           file_to_shock function. shock_id - the ID of the new Shock node.
           handle - the new handle, if created. Null otherwise.
           node_file_name - the name of the file stored in Shock. size - the
           size of the file stored in shock.) -> structure: parameter
           "shock_id" of String, parameter "handle" of type "Handle" (A
           handle for a file stored in Shock. hid - the id of the handle in
           the Handle Service that references this shock node id - the id for
           the shock node url - the url of the shock server type - the type
           of the handle. This should always be shock. file_name - the name
           of the file remote_md5 - the md5 digest of the file.) ->
           structure: parameter "hid" of String, parameter "file_name" of
           String, parameter "id" of String, parameter "url" of String,
           parameter "type" of String, parameter "remote_md5" of String,
           parameter "node_file_name" of String, parameter "size" of String
        """
        job_id = self._file_to_shock_mass_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _copy_shock_node_submit(self, params, context=None):
        return self._client._submit_job(
             'DataFileUtil.copy_shock_node', [params],
             self._service_ver, context)

    def copy_shock_node(self, params, context=None):
        """
        Copy a Shock node.
        :param params: instance of type "CopyShockNodeParams" (Input for the
           copy_shock_node function. Required parameters: shock_id - the id
           of the node to copy. Optional parameters: make_handle - make a
           Handle Service handle for the shock node. Default false.) ->
           structure: parameter "shock_id" of String, parameter "make_handle"
           of type "boolean" (A boolean - 0 for false, 1 for true. @range (0,
           1))
        :returns: instance of type "CopyShockNodeOutput" (Output of the
           copy_shock_node function. shock_id - the id of the new Shock node.
           handle - the new handle, if created. Null otherwise.) ->
           structure: parameter "shock_id" of String, parameter "handle" of
           type "Handle" (A handle for a file stored in Shock. hid - the id
           of the handle in the Handle Service that references this shock
           node id - the id for the shock node url - the url of the shock
           server type - the type of the handle. This should always be shock.
           file_name - the name of the file remote_md5 - the md5 digest of
           the file.) -> structure: parameter "hid" of String, parameter
           "file_name" of String, parameter "id" of String, parameter "url"
           of String, parameter "type" of String, parameter "remote_md5" of
           String
        """
        job_id = self._copy_shock_node_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _own_shock_node_submit(self, params, context=None):
        return self._client._submit_job(
             'DataFileUtil.own_shock_node', [params],
             self._service_ver, context)

    def own_shock_node(self, params, context=None):
        """
        Gain ownership of a Shock node.
        Returns a shock node id which is owned by the caller, given a shock
        node id.
        If the shock node is already owned by the caller, returns the same
        shock node ID. If not, the ID of a copy of the original node will be
        returned.
        If a handle is requested, the node is already owned by the caller, and
        a handle already exists, that handle will be returned. Otherwise a new
        handle will be created and returned.
        :param params: instance of type "OwnShockNodeParams" (Input for the
           own_shock_node function. Required parameters: shock_id - the id of
           the node for which the user needs ownership. Optional parameters:
           make_handle - make or find a Handle Service handle for the shock
           node. Default false.) -> structure: parameter "shock_id" of
           String, parameter "make_handle" of type "boolean" (A boolean - 0
           for false, 1 for true. @range (0, 1))
        :returns: instance of type "OwnShockNodeOutput" (Output of the
           own_shock_node function. shock_id - the id of the (possibly new)
           Shock node. handle - the handle, if requested. Null otherwise.) ->
           structure: parameter "shock_id" of String, parameter "handle" of
           type "Handle" (A handle for a file stored in Shock. hid - the id
           of the handle in the Handle Service that references this shock
           node id - the id for the shock node url - the url of the shock
           server type - the type of the handle. This should always be shock.
           file_name - the name of the file remote_md5 - the md5 digest of
           the file.) -> structure: parameter "hid" of String, parameter
           "file_name" of String, parameter "id" of String, parameter "url"
           of String, parameter "type" of String, parameter "remote_md5" of
           String
        """
        job_id = self._own_shock_node_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _ws_name_to_id_submit(self, name, context=None):
        return self._client._submit_job(
             'DataFileUtil.ws_name_to_id', [name],
             self._service_ver, context)

    def ws_name_to_id(self, name, context=None):
        """
        Translate a workspace name to a workspace ID.
        :param name: instance of String
        :returns: instance of Long
        """
        job_id = self._ws_name_to_id_submit(name, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _save_objects_submit(self, params, context=None):
        return self._client._submit_job(
             'DataFileUtil.save_objects', [params],
             self._service_ver, context)

    def save_objects(self, params, context=None):
        """
        Save objects to the workspace. Saving over a deleted object undeletes
        it.
        :param params: instance of type "SaveObjectsParams" (Input parameters
           for the "save_objects" function. Required parameters: id - the
           numerical ID of the workspace. objects - the objects to save. The
           object provenance is automatically pulled from the SDK runner.) ->
           structure: parameter "id" of Long, parameter "objects" of list of
           type "ObjectSaveData" (An object and associated data required for
           saving. Required parameters: type - the workspace type string for
           the object. Omit the version information to use the latest
           version. data - the object data. Optional parameters: One of an
           object name or id. If no name or id is provided the name will be
           set to 'auto' with the object id appended as a string, possibly
           with -\d+ appended if that object id already exists as a name.
           name - the name of the object. objid - the id of the object to
           save over. meta - arbitrary user-supplied metadata for the object,
           not to exceed 16kb; if the object type specifies automatic
           metadata extraction with the 'meta ws' annotation, and your
           metadata name conflicts, then your metadata will be silently
           overwritten. hidden - true if this object should not be listed
           when listing workspace objects.) -> structure: parameter "type" of
           String, parameter "data" of unspecified object, parameter "name"
           of String, parameter "objid" of Long, parameter "meta" of mapping
           from String to String, parameter "hidden" of type "boolean" (A
           boolean - 0 for false, 1 for true. @range (0, 1))
        :returns: instance of list of type "object_info" (Information about
           an object, including user provided metadata. objid - the numerical
           id of the object. name - the name of the object. type - the type
           of the object. save_date - the save date of the object. ver - the
           version of the object. saved_by - the user that saved or copied
           the object. wsid - the id of the workspace containing the object.
           workspace - the name of the workspace containing the object. chsum
           - the md5 checksum of the object. size - the size of the object in
           bytes. meta - arbitrary user-supplied metadata about the object.)
           -> tuple of size 11: parameter "objid" of Long, parameter "name"
           of String, parameter "type" of String, parameter "save_date" of
           String, parameter "version" of Long, parameter "saved_by" of
           String, parameter "wsid" of Long, parameter "workspace" of String,
           parameter "chsum" of String, parameter "size" of Long, parameter
           "meta" of mapping from String to String
        """
        job_id = self._save_objects_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _get_objects_submit(self, params, context=None):
        return self._client._submit_job(
             'DataFileUtil.get_objects', [params],
             self._service_ver, context)

    def get_objects(self, params, context=None):
        """
        Get objects from the workspace.
        :param params: instance of type "GetObjectsParams" (Input parameters
           for the "get_objects" function. Required parameters: object_refs -
           a list of object references in the form X/Y/Z, where X is the
           workspace name or id, Y is the object name or id, and Z is the
           (optional) object version. In general, always use ids rather than
           names if possible to avoid race conditions. Optional parameters:
           ignore_errors - ignore any errors that occur when fetching an
           object and instead insert a null into the returned list.) ->
           structure: parameter "object_refs" of list of String, parameter
           "ignore_errors" of type "boolean" (A boolean - 0 for false, 1 for
           true. @range (0, 1))
        :returns: instance of type "GetObjectsResults" (Results from the
           get_objects function. list<ObjectData> data - the returned
           objects.) -> structure: parameter "data" of list of type
           "ObjectData" (The data and supplemental info for an object.
           UnspecifiedObject data - the object's data or subset data.
           object_info info - information about the object.) -> structure:
           parameter "data" of unspecified object, parameter "info" of type
           "object_info" (Information about an object, including user
           provided metadata. objid - the numerical id of the object. name -
           the name of the object. type - the type of the object. save_date -
           the save date of the object. ver - the version of the object.
           saved_by - the user that saved or copied the object. wsid - the id
           of the workspace containing the object. workspace - the name of
           the workspace containing the object. chsum - the md5 checksum of
           the object. size - the size of the object in bytes. meta -
           arbitrary user-supplied metadata about the object.) -> tuple of
           size 11: parameter "objid" of Long, parameter "name" of String,
           parameter "type" of String, parameter "save_date" of String,
           parameter "version" of Long, parameter "saved_by" of String,
           parameter "wsid" of Long, parameter "workspace" of String,
           parameter "chsum" of String, parameter "size" of Long, parameter
           "meta" of mapping from String to String
        """
        job_id = self._get_objects_submit(params, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _versions_submit(self, context=None):
        return self._client._submit_job(
             'DataFileUtil.versions', [],
             self._service_ver, context)

    def versions(self, context=None):
        """
        Get the versions of the Workspace service and Shock service.
        :returns: multiple set - (1) parameter "wsver" of String, (2)
           parameter "shockver" of String
        """
        job_id = self._versions_submit(context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result']

    def status(self, context=None):
        job_id = self._client._submit_job('DataFileUtil.status', 
            [], self._service_ver, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]
